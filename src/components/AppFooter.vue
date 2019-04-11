<template>
	<section class="Footer">
		<div class="App__inner Footer__inner">

			<b-link
				class="Footer__link"
				href="https://github.com/andrewlew1s/hmc-transcribers"
				target="_blank">
				An HMC-Transcribers project.
			</b-link>

			<div class="Footer__icons">
				<b-link
					class="Footer__icon"
					href="https://github.com/andrewlew1s/hmc-transcribers"
					target="_blank"
					title="Follow on Twitter!">
					<img alt="Vue logo" src="../assets/logo.png"/>
				</b-link>
			</div>

		</div>
	</section>
</template>

<script>
export default {
	data() {
		return {
			icons: [
				{
					name: 'myIcon'
				}
			]
		};
	}
};
</script>

<style lang="scss">
@import '../settings';

$height: $Footer-Height;
$background: $Background;
$textColour: $Highlight-Colour;

.Footer{
	border-top: 1px solid $Grey;
	background: $background;
	color: $textColour;
	height: $height;
	width: 100%;
	float: left;

	&__inner {
		padding-top: 1.5em;
	}

	&__icons {
		float: right;
	}

	&__icon {
		margin: 0 8px;
		float: left;

		> img {
			width: 24px;
		}

	}

	&__link {
		color: $textColour;

		&:hover {
			color: $textColour;
			text-decoration: none;
		}

	}
}

</style>
