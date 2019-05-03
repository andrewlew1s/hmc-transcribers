<template>
	<section class="Page1">
		<landing-image class="Page1__image"/>
		<div class="Page1__content">
			<v-container > 				
				<img id="Page1__content" src="../../assets/logo.png">				
				<div class="Page1__content__header">
					<h1>Upload a business card</h1>
				</div>
				<input type="file" name='file' @change="onFileSelected">
				<v-btn @click="onUpload">Upload</v-btn>
			</v-container>
			<div class="Page2__card">
				<v-layout>
					<v-flex xs12 sm6 offset-sm3>
						<v-card>
							<v-img
								height="200px"
								v-bind:src="this.imageURL">
								<v-container fill-height fluid>
								</v-container>
							</v-img>
							<v-card-actions>
								<p>Is this your card?</p>
								<v-btn @click="updateData" flat color="black">Yes</v-btn>
							</v-card-actions>
						</v-card>
					</v-flex>
				</v-layout>
			</div>
			<v-btn to="/display">See results</v-btn>
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
		imageURL: '',
	}
  },
  components: {
	LandingImage   
  },
  methods: {

	sleep(milliseconds) {
		var start = new Date().getTime();
		for (var i = 0; i < 1e7; i++) {
			if ((new Date().getTime() - start) > milliseconds){
			break;
			}
		}
	},

	onFileSelected(event) {
		this.selectedFile = event.target.files[0]
		console.log(this.selectedFile)
		const fileReader = new FileReader()
	},
	onUpload() {
		var filename = this.selectedFile.name
		var storageRef = firebase.storage().ref('cards/' + filename)
		console.log(storageRef)
		storageRef.put(this.selectedFile)
		this.sleep(4000)
		storageRef.getDownloadURL().then((imageURL) => {
			console.log(imageURL)
  			this.imageURL = imageURL
		})	
	},
	updateData() {
		
		var filename = this.selectedFile.name
		axios.get('http://ec2-52-53-126-176.us-west-1.compute.amazonaws.com:8000/transcribe', {
		params: {
			name: filename
			}
		})
		.then(res => {
			console.log(res.data)
			for (var i = 0; i<res.data.length; i++) {
				console.log(res.data[i])
			}
			if (res.data.first_name) {
				var firstString = JSON.stringify(res.data.first_name[0])
				this.$store.commit('updateFirst', firstString)
			}
			if (res.data.last_name) {
				var lastString = JSON.stringify(res.data.last_name[0])
				this.$store.commit('updateLast', lastString)
			}
			if (res.data.email_id) {
				var emailString = JSON.stringify(res.data.email_id[0])
				this.$store.commit('updateEmail', emailString)
			}
			if (res.data.office_address) {
				var addressString = JSON.stringify(res.data.office_address[0])
				this.$store.commit('updateAddress', addressString)
			}
			if (res.data.phone) {
				var phoneString = JSON.stringify(res.data.phone[0])
				this.$store.commit('updatePhone', phoneString)
			}
			if (res.data.state) {
				var stateString = JSON.stringify(res.data.state[0])
				this.$store.commit('updateState', stateString)
			}
			if (res.data.title) {
				var titleString = JSON.stringify(res.data.title[0])
				this.$store.commit('updateTitle', titleString)
			}			
		}).catch(error => console.log(error))
	}
  }
}
</script>

<style lang="scss">

.Page1 {
	
	&__image {
		width: 100%;
		height: calc(100vh - 3.5rem);
		margin-bottom: 1rem;
	}

	&__intro {
		width: 80%;
		margin: -4rem 10% 2rem 10%;
		text-align: center;
	}

	&__content {
		position: relative;
		z-index: 1;
		padding: 1rem;
		margin-top: 2rem;

		&__header {
			margin-top: 2rem;
			margin-bottom: 1rem;
		}
	}
}

</style>
