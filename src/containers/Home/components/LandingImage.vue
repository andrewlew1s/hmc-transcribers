<template>
	<section class="LandingImage">
		<v-container class="LandingImage__inner">

			<h1 class="LandingImage__text">We are the BizNiz card transcribers and we <span class="LandingImage__text--alt">transcribe business cards.</span></h1>

			<section v-scroll-to="'#Page1__content'" class="LandingImage__readMore">
				<span>Discover <span class="LandingImage--altColour">More</span></span>
				<v-icon v-text="'arrow_downwards'" color="highlight" small/>
			</section>
		</v-container>
	</section>
</template>

<style lang="scss">

.LandingImage {
	
	width: 100%;
	margin-top: 0.5rem;
	height: 100vh;
	background-image: url('../../../assets/landingimage.jpg');
	background-size: cover;
	background-position: center;
	display: flex;
	flex-direction: column;
	justify-content: center;

	&--altColour {
		color: maroon;
	}

	&__inner {
		display: flex;
		flex-direction: column;
	}

	&__text {
		font-size: 3rem;
		letter-spacing: 0.1rem;
		line-height: 4rem;
		color: black;
		font-weight: bold;
		margin-top: 25vh;

		&--alt {
		color: maroon;
		}
	}

	&__readMore {
		justify-self: center;
		color: black;
		margin-top: 5vh;
		display: flex;
		flex-direction: column;
		text-align: center;
		font-weight: bold;
		letter-spacing: 0.1rem;
		text-transform: uppercase;
		cursor: pointer;
	}
}

</style>

