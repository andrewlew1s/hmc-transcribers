<template>
	<section class="Page1">
		<landing-image class="Page1__image"/>
		<div class="Page1__content">
			<v-container >
				<img id="Page1__content" src="../../assets/logo.png">
				<div class="Page1__content__header">
					<h1>Upload a business card</h1>
				</div>
				<div id="v-progress-circular" class="Page1__content__progress">
					<input type="file" name='file' @change="onFileSelected">
					<v-btn @click="onUpload">Upload</v-btn>
					<v-progress-circular
					v-bind:style="{ visibility: computedVisibility }"
					:width="3"
					color="red"
					indeterminate>
					</v-progress-circular>
				</div>
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
		visibility: 'hidden'
	}
  },
  computed: {
    computedVisibility: function () {
      return this.visibility;
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
	},
	onUpload() {
		this.visibility = 'visible'
		var filename = this.selectedFile.name
		var storageRef = firebase.storage().ref('cards/' + filename)
		storageRef.put(this.selectedFile)
		this.sleep(2000)
		storageRef.getDownloadURL().then((imageURL) => {
			this.visibility = 'hidden'
			this.imageURL = imageURL
		})
		this.sleep(1000)
		storageRef.getDownloadURL().then((imageURL) => {
			this.imageURL = imageURL
			this.visibility = 'hidden'
			return
		})
		this.sleep(1000)
		storageRef.getDownloadURL().then((imageURL) => {
			this.imageURL = imageURL
			this.visibility = 'hidden'
			return
		})
		this.sleep(1000)
		storageRef.getDownloadURL().then((imageURL) => {
			this.imageURL = imageURL
			this.visibility = 'hidden'
			return
		})
	},
	updateData() {

		var filename = this.selectedFile.name
		axios.get('http://ec2-54-183-194-82.us-west-1.compute.amazonaws.com:8000/transcribe', {
		params: {
			name: filename
			}
		})
		.then(res => {
			var stringRes = res.data.toString()
			if (stringRes.indexOf("File name does not exist") > -1) {
				try{
					var errorOCR = 'FILE UPLOAD ERROR. Sorry, we encountered an error reaching your file. Please try again or with another image.'
					alert(errorOCR)
				}catch(throw_error){
					return throw_error
				}
			}
			if (stringRes.indexOf("Unable to read") > -1) {
				try{
					var a = 'OCR ERROR. Sorry, we encountered an error reading text from your image. Please make sure the image is upright, clear and evenly lit.'
					alert(a)
				}catch(throw_error){
					return throw_error
				}
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
			if (res.data.office_address2) {
				var addressString2 = JSON.stringify(res.data.office_address2[0])
				this.$store.commit('updateAddress2', addressString2)
			}
			if (res.data.phone) {
				var phoneString = JSON.stringify(res.data.phone[0])
				this.$store.commit('updatePhone', phoneString)
			}
			if (res.data.fax) {
				var faxString = JSON.stringify(res.data.fax[0])
				this.$store.commit('updateFax', faxString)
			}
			if (res.data.city) {
				var cityString = JSON.stringify(res.data.city[0])
				this.$store.commit('updateCity', cityString)
			}
			if (res.data.state) {
				var stateString = JSON.stringify(res.data.state[0])
				this.$store.commit('updateState', stateString)
			}
			if (res.data.zipcode) {
				var zipString = JSON.stringify(res.data.zipcode[0])
				this.$store.commit('updateZip', zipString)
			}
			if (res.data.country) {
				var countryString = JSON.stringify(res.data.country[0])
				this.$store.commit('updateCountry', countryString)
			}
			if (res.data.title) {
				var titleString = JSON.stringify(res.data.title[0])
				this.$store.commit('updateTitle', titleString)
			}
			if (res.data.company) {
				var companyString = JSON.stringify(res.data.company[0])
				this.$store.commit('updateCompany', companyString)
			}
		}).catch()
	}
  }
}
</script>

<style lang="scss">

.v-progress-circular {

    margin: 1rem;

}

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
		padding: 0.5rem;
		margin-top: 2.5rem;

		&__header {
			margin-top: 2rem;
			margin-bottom: 0.5rem;
		}
	}
}

</style>
