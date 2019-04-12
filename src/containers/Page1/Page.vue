<template>
	<section class="Page1">
		<landing-image class="Page1__image"/>
		<div class="Page1__content">
			<v-container>
				<div class="Page1__content__logo">
					<img alt="Vue logo" src="../../assets/logo.png">
				</div>
				<div class="Page1__content__header">
					<h1>Upload a business card</h1>
				</div>
				<input type="file" name='file' @change="onFileSelected">
				<button @click="onUpload" to="/display">Upload</button>
			</v-container>
		</div>
	</section>
</template>

<script>
import axios from 'axios';
import * as firebase from 'firebase'
import LandingImage from './components/LandingImage';

export default {

  name: 'app',
  data () {
	return {
		selectedFile: null,
		imageUrl: '',
	}
  },
  components: {
	LandingImage   
  },
  methods: {
	onFileSelected(event) {
		this.selectedFile = event.target.files[0]
		console.log(this.selectedFile)
		const fileReader = new FileReader()
		fileReader.addEventListener('load', () => {
			this.imageUrl = fileReader.result
			console.log(this.imageUrl)
		})
	},
	onUpload() {
		var filename = this.selectedFile.name
		console.log(filename)
		var storageRef = firebase.storage().ref('cards/' + filename)
		console.log(storageRef)
		var uploadTask = storageRef.put(this.selectedFile)

		var downloadURL = uploadTask.snapshot.downloadURL
		console.log(downloadURL)
		axios.get('http://127.0.0.1:5000/fields')
			.then(res => {
				console.log(res)
			})
	}
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
		// padding: 3rem;
	}

	&__content {
		// padding: 1rem;
		margin-top: 2rem;
		position: relative;
		z-index: 1;

		&__logo {
			padding: 6rem;
		}

		&__header {
			margin-bottom: 2rem;
		}

	}

}

</style>
