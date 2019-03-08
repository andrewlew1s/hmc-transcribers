<template>
	<div class="Page1">
		<img alt="Vue logo" src="../../assets/logo.png">
		<h1>Upload your business card now</h1>
		<Browse class="browse"/>
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


</style>
