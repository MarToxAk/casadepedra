/* http://github.com/mindmup/bootstrap-wysiwyg */
/*global jQuery, $, FileReader*/
/*jslint browser:true*/
(function ($) {
	'use strict';
	var readFileIntoDataUrl = function (fileInfo) {
		var loader = $.Deferred(),
			fReader = new FileReader();
		fReader.onload = function (e) {
			loader.resolve(e.target.result);
		};
		fReader.onerror = loader.reject;
		fReader.onprogress = loader.notify;
		fReader.readAsDataURL(fileInfo);
		return loader.promise();
	};
	$.fn.cleanHtml = function () {
		var html = $(this).html();
		return html && html.replace(/(<br>|\s|<div><br><\/div>|&nbsp;)*$/, '');
	};
	$.fn.wysiwyg = function (userOptions) {
		var editor = this,
			selectedRange,
			options,
			toolbarBtnSelector,
			updateToolbar = function () {
				if (options.activeToolbarClass) {
					$(options.toolbarSelector).find(toolbarBtnSelector).each(function () {
						var command = $(this).data(options.commandRole);
						console.log(document.queryCommandState(command))
						if (document.queryCommandState(command)) {
							$(this).addClass(options.activeToolbarClass);
						} else {
							$(this).removeClass(options.activeToolbarClass);
						}
					});
				}
			},
			execCommand = function (commandWithArgs, valueArg) {
				var commandArr = commandWithArgs.split(' '),
					command = commandArr.shift(),
					args = commandArr.join(' ') + (valueArg || '');
				document.execCommand(command, 0, args);
				updateToolbar();
			},
			bindHotkeys = function (hotKeys) {
				$.each(hotKeys, function (hotkey, command) {
					editor.keydown(hotkey, function (e) {
						if (editor.attr('contenteditable') && editor.is(':visible')) {
							e.preventDefault();
							e.stopPropagation();
							execCommand(command);
						}
					}).keyup(hotkey, function (e) {
						if (editor.attr('contenteditable') && editor.is(':visible')) {
							e.preventDefault();
							e.stopPropagation();
						}
					});
				});
			},
			getCurrentRange = function () {
				var sel = window.getSelection();
				//console.log(sel)
				if (sel.getRangeAt && sel.rangeCount) {
					////console.log(Object.values(sel.getRangeAt(0)))
					//var selRange = selObj.getRangeAt(0);

					return sel.getRangeAt(0);
					
				}
			},
			saveSelection = function () {
				selectedRange = getCurrentRange();
			},
			restoreSelection = function () {
				var selection = window.getSelection();
				if (selectedRange) {
					try {
						selection.removeAllRanges();
					} catch (ex) {
						document.body.createTextRange().select();
						document.selection.empty();
					}

					selection.addRange(selectedRange);
				}
			},
			insertFiles = function (files) {
				editor.focus();
				$.each(files, function (idx, fileInfo) {
					if (/^image\//.test(fileInfo.type)) {
						$.when(readFileIntoDataUrl(fileInfo)).done(function (dataUrl) {
							execCommand('insertimage', dataUrl);
						}).fail(function (e) {
							options.fileUploadError("file-reader", e);
						});
					} else {
						options.fileUploadError("unsupported-file-type", fileInfo.type);
					}
				});
			},
			markSelection = function (input, color) {
				restoreSelection();
				if (document.queryCommandSupported('hiliteColor')) {
					document.execCommand('hiliteColor', 0, color || 'transparent');
				}
				saveSelection();
				input.data(options.selectionMarker, color);
			},
			bindToolbar = function (toolbar, options) {
				toolbar.find(toolbarBtnSelector).click(function () {
					var newValue = this.name; /* ugly but prevents fake double-calls due to selection restoration */
					var ta = $('#id_cotacao_texto').get(0);
					var sel = ta.value.substring(ta.selectionStart, ta.selectionEnd);

					this.value = '';
					//console.log(this.name)
					 alert(sel);
					 restoreSelection();
					if (newValue == "bold" ) {
						editor.focus();
						console.log(editor.focus());
						var newValue = ('*'+sel+'*')
						execCommand($(this).data(options.commandRole), newValue);
					} else if (newValue == 'italic') {
						editor.focus();
						var newValue = ('_'+sel+'_')
						execCommand($(this).data(options.commandRole), newValue);
					} else if (newValue == 'strikethrough') {
						editor.focus();
						var newValue = ('~'+sel+'~')
						execCommand($(this).data(options.commandRole), newValue);
					} else if (newValue == 'monospace') {
						editor.focus();
						var newValue = ("'''"+sel+"'''")
						execCommand($(this).data(options.commandRole), newValue);
					} else {
						editor.focus();
						execCommand($(this).data(options.commandRole), newValue);
						if ( newValue == "$Check_In" ){
							$("#id_check_in").prop('checked', true);
						} else if ( newValue == "$Check_Out" ){
							$("#id_check_out").prop('checked', true);
						} else if ( newValue == "$Num_Dias" ){
							$("#id_num_dias").prop('checked', true);
						} else if ( newValue == "$Num_Criancas" ){
							$("#id_num_criancas").prop('checked', true);
						} else if ( newValue == "$Idade_Crianca" ){
							$("#id_idade_crianca").prop('checked', true);
						} else if ( newValue == "$Num_Pessoas" ){
							$("#id_num_pessoas").prop('checked', true);
						} else if ( newValue == "$Valor_Total" ){
							$("#id_valor_total").prop('checked', true);
						} else if ( newValue == "$Valor_Real" ){
							$("#id_valor_real").prop('checked', true);
						} else if ( newValue == "$Valor_Desconto" ){
							$("#id_valor_desconto").prop('checked', true);
						} else if ( newValue == "$Valor_Da_Parcelas" ){
							$("#id_valor_da_parcelas").prop('checked', true);
						} else if ( newValue == "$Valor_Da_Parcelas_Menos_Etrada" ){
							$("#id_valor_da_parcelas_menos_etrada").prop('checked', true);
						} else if ( newValue == "$Valor_50Porc" ){
							$("#id_valor_50porc").prop('checked', true);
						} else if ( newValue == "$Num_Parcela" ){
							$("#id_num_parcela").prop('checked', true);
						} else if ( newValue == "$Num_Parcela_Mais_1" ){
							$("#id_num_parcela_mais_1").prop('checked', true);
						} else if ( newValue == "$Porcentagem" ){
							$("#id_porcentagem").prop('checked', true);
						} else if ( newValue == "$Porcentagem_Mais_5" ){
							$("#id_porcentagem_mais_5").prop('checked', true);
						}	
						saveSelection();
					}
				});
			},
			initFileDrops = function () {
				editor.on('dragenter dragover', false)
					.on('drop', function (e) {
						var dataTransfer = e.originalEvent.dataTransfer;
						e.stopPropagation();
						e.preventDefault();
						if (dataTransfer && dataTransfer.files && dataTransfer.files.length > 0) {
							insertFiles(dataTransfer.files);
						}
					});
			};
		options = $.extend({}, $.fn.wysiwyg.defaults, userOptions);
		toolbarBtnSelector = 'a[data-' + options.commandRole + '],button[data-' + options.commandRole + '],input[type=button][data-' + options.commandRole + ']';
		bindHotkeys(options.hotKeys);
		if (options.dragAndDropImages) {
			initFileDrops();
		}
		bindToolbar($(options.toolbarSelector), options);
		editor.attr('contenteditable', true)
			.on('mouseup keyup mouseout', function () {
				saveSelection();
				updateToolbar();
			});
		$(window).bind('touchend', function (e) {
			var isInside = (editor.is(e.target) || editor.has(e.target).length > 0),
				currentRange = getCurrentRange(),
				clear = currentRange && (currentRange.startContainer === currentRange.endContainer && currentRange.startOffset === currentRange.endOffset);
				
				
			if (!clear || isInside) {
				//console.log(isInside);
				saveSelection();
				updateToolbar();
			}
		});
		return this;
	};
	$.fn.wysiwyg.defaults = {
		hotKeys: {
			'ctrl+b meta+b': 'bold',
			'ctrl+i meta+i': 'italic',
			'ctrl+u meta+u': 'underline',
			'ctrl+z meta+z': 'undo',
			'ctrl+y meta+y meta+shift+z': 'redo',
			'ctrl+l meta+l': 'justifyleft',
			'ctrl+r meta+r': 'justifyright',
			'ctrl+e meta+e': 'justifycenter',
			'ctrl+j meta+j': 'justifyfull',
			'shift+tab': 'outdent',
			'tab': 'indent'
		},
		toolbarSelector: '[data-role=editor-toolbar]',
		commandRole: 'edit',
		activeToolbarClass: 'btn-info',
		selectionMarker: 'edit-focus-marker',
		selectionColor: 'darkgrey',
		dragAndDropImages: true,
		fileUploadError: function (reason, detail) { console.log("File upload error", reason, detail); }
	};
}(window.jQuery));