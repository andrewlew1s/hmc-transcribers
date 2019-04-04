<template>
	<div class="Page1">
		<img alt="Vue logo" src="../../assets/logo.png">
		<div  class="Page1__header">
			<h1>Upload your business card now</h1>
		</div>
		<Browse class="browse"/>
		<div  class="Page1__displayButton">
			<router-link to="/display" tag="button">To fields!</router-link>
		</div>
	</div>
</template>

<script>
import Browse from '../../components/Browse.vue'


export default {

  name: 'app',
  components: {
	Browse   
  }
}

</script>

<style lang="scss">

.Page1 {
	
	&__displayButton {
		padding: 2rem;
	}
	&__header {
		padding: 2rem;
	}
}


</style>
