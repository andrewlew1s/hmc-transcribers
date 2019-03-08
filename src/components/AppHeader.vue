<template>
<div class="Header">

	<div class="App__inner Header__inner">

		<menue
			class="Header__menu"
			:auto="true"/>

	</div>

</div>
</template>

<script>
import Menue from './Menue';

export default {
	components: {
		Menue
	}
};
</script>

<style lang="scss">
@import '../settings';

.Header{
	$height: 40px;
	background: $Highlight;
	height: $height;
	position: relative;
	z-index: 10;

	&__inner {
		height: $height;
	}

	&__logo{
		height: $height / 2;
		margin: auto;
        margin-top: $height / 10;
        display: block;
	}

	&__menu{
		margin-top: $height/20
	}

}

</style>
