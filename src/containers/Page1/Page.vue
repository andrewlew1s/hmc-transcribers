<template>
	<section class="Page1">
		<landing-image class="Page1__image"/>
		<div class="Page1__content">
			<v-container>
				<div class="Page1__content__logo">
					<img alt="Vue logo" src="../../assets/logo.png">
				</div>
				<section id="Page1__content" class="Page1__intro">
					<Browse class="Page1__browse"/>
				</section>
			</v-container>
		</div>
	</section>
</template>

<script>
import Browse from '../../components/Browse.vue'
import LandingImage from './components/LandingImage';

export default {

  name: 'app',
  components: {
	Browse,
	LandingImage   
  }
}
</script>

<style lang="scss">

.Page1 {
	

	&__image {
		width: 100%;
		height: calc(100vh - 5.5rem);
		margin-bottom: 1rem;
	}

	&__intro {
		width: 80%;
		margin: -4rem 10% 2rem 10%;
		text-align: center;
		padding: 2rem 3rem;
	}

	&__content {
		margin-top: 2rem;
		position: relative;
		z-index: 1;

		&__logo {
			padding: 7rem;
		}

	}

}

</style>
