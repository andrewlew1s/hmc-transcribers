<template>
	<div class="About">
		<div class="About__header">
			<h1>Meet the Transcribers!</h1>
		</div>
		<div class="About__team">
			<team />
		</div>
	</div>
</template>

<script>
import Team from '../../components/Team';


export default {
	components: {
		Team
	}
}
</script>

<style lang="scss">

.About {

	display: flex;
	flex-direction: column;
	align-items: center;

	&__header {
		margin-top: 2rem;
	}

	&__team {

	}
}
</style>

