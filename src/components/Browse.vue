<template>
  <div>
    <b-form-file
      v-model="file"
      :state="Boolean(file)"
      placeholder="Choose a file..."
      drop-placeholder="Drop file here..."
      accept=".jpg, .png, .pdf"
    />
  </div>
</template>

<script>
  export default {
    data() {
      return {
        file: null,
        file2: null
      }
    }
  }
</script>

