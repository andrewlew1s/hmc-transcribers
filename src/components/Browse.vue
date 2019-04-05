<template>
  <div class="Browse">
    <div  class="Browse__header">
			<h1>Upload a business card</h1>
		</div>
    <div  class="Browse__form">
      <b-form-file 
        v-model="file"
        accept=".jpg, .png, .pdf" 
        drop-placeholder="Drop the file!" 
        class="mt-3" 
        plain
        >
      </b-form-file>
    </div>
    <div class="Browse__button">
			<v-btn color="grey" to="/display">Transcribe</v-btn>
		</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        file: null
      }
    }
  }
</script>

<style lang="scss">

.Browse {

  &__header {
		padding: 1rem;
  }
  
  &__button {
		padding: 2rem;
  }
  
   &__form {
		margin-left: 4rem;
	}
}
</style>


