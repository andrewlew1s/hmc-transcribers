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
			</v-container>
				<div class="Page2__card">
				<v-layout>
					<v-flex xs12 sm6 offset-sm3>
						<v-card>
							<v-img
								height="200px"
								src="https://images.pexels.com/photos/326569/pexels-photo-326569.jpeg?cs=srgb&dl=adult-blank-business-326569.jpg&fm=jpg">
								<v-container fill-height fluid>
								</v-container>
							</v-img>
							<v-card-actions>
								<p>Is this your card?</p>
								<v-btn @click="updateData" flat color="black">Yes</v-btn>
							</v-card-actions>
						</v-card>
						<v-btn @click="onUpload" to="/display">See results</v-btn>
					</v-flex>
				</v-layout>
			</div>
		</div>
	</section>
</template>

<script>
import axios from 'axios'
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
		
		// var downloadURL = uploadTask.snapshot.downloadURL
		// console.log(downloadURL)
	},
	updateData() {
		axios.get('https://hidden-garden-54983.herokuapp.com/fields')
		.then(res => {
			console.log(res.data)
			console.log(res.data.email_id[0])
			for (var i = 0; i<res.data.length; i++) {
				console.log(res.data[i])
			}
			var firstString = JSON.stringify(res.data.first_name[0])
			var lastString = JSON.stringify(res.data.last_name[0])
			var emailString = JSON.stringify(res.data.email_id[0])
			console.log(emailString)
			var addressString = JSON.stringify(res.data.office_address[0])
			var phoneString = JSON.stringify(res.data.phone[0])
			var stateString = JSON.stringify(res.data.state[0])
			var titleString = JSON.stringify(res.data.title[0])
			this.$store.commit('updateFirst', firstString)
			this.$store.commit('updateLast', lastString)
			this.$store.commit('updateEmail', emailString)
			this.$store.commit('updateAddress', addressString)
			this.$store.commit('updatePhone', phoneString)
			this.$store.commit('updateState', stateString)
			this.$store.commit('updateTitle', titleString)
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
