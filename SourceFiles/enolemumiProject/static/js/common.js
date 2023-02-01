$(function(){
	$('.filter-button').click(function() {
		$('.catalog-filter').toggleClass('opened');
	});
	$('.catalog-filter .item .name').click(function() {
		$(this).toggleClass('active');
		$(this).next('.content').slideToggle();
	});
	$('.faq-block .item .name').click(function() {
		$(this).toggleClass('active');
		$(this).parent().toggleClass('active');
		$(this).next('.text').slideToggle();
	});
	$('.upload').click(function(){
		$(this).next('input').click();
	});
	$('.menubg').click(function() {
		$('.menubg').fadeOut();
		$('.header .menu-button').removeClass('active');
		$('.header ul').removeClass('opened');
		$('.top-menu').removeClass('opened');
	});
	$('.header .menu-button').click(function() {
		$('.menubg').fadeIn();
		$('.header .menu-button').addClass('active');
		$('.header ul').addClass('opened');
		$('.top-menu').addClass('opened');
	});
	$('.index-page-slider').slick({
		arrows: false,
		dots: true
	});
	$('.reg-page .list .slider').slick({
		arrows: false,
		dots: true
	});
});