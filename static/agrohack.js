$(document).ready(function() {
	$('.background').hide();
	$('.file_title').hide();
	$('.download_files').hide();

	$('.route').click(function() {
		let form = $('form');
		$.ajax({
			url: form.attr('action'),
			method: 'POST',
			data: form.serialize(),
			success: function(res) {
				$('.background').show();
				$.ajax({
					url: '/result?id='+res,
					method: 'GET',
					success: function(res) {
						$('.background').hide();
						$('.file_title').show();
						$('.download_files').show();
						$('.download_file').html(res);
					},
					complete: function(xhr, msg) {
						if (xhr.status != 200) alert(xhr.responseText || msg);
					}
				});
			},
			complete: function(xhr, msg) {
				if (xhr.status != 200) alert(xhr.responseText || msg);
			}
		});
	});
});
