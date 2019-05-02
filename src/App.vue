<template>
  <div id="app">
	<div class="App__inner">

		<app-header class="App__header"/>

		<router-view class="App__wrapper"/>

		<app-footer class="App__footer"/>

	</div>
  </div>
</template>

<script>

import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';

export default {


  name: 'app',
  components: {
    AppHeader,
    AppFooter
    
  }
}
</script>

<style lang="scss">
@import './settings';
$footerHeight: $Footer-Height;
$headerHeight: $Header-Height;
$frameWidth: $Frame-Width;
$mobileWidth: $Mobile-Width;
$textColour: $Text-Colour;
$backgroundColour: $Background-Colour;
$fontFamily: $Font-Family;
$highlightColour: $Highlight-Colour;
$shadowColour: $Shadow-Colour;

$footerPadding: 60px;

.App {
	font-family: $fontFamily;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	

	&__inner {
		
		width: 100%;
		overflow: control;
		text-align: center;
		
	}

	&__wrapper {
		min-height: calc(100vh - #{$footerHeight});
		font-family: $fontFamily;
		background: #ffffff;
		float: left;
		width: 100%;
		padding-bottom: $footerPadding;
	}

	&__header {
		font-family: $fontFamily;
	}

	&__footer {
		font-family: $fontFamily;
	}

}
</style>
