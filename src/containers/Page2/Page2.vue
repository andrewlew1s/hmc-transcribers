<template>
	<div class="Page2">
			<v-data-table
				:headers="headers"
				:items="fields"
				class="elevation-1">
				<template v-slot:no-data>
					<v-alert :value="true" color="error" icon="warning">
						Sorry, nothing to display here :(
					</v-alert>
				</template>
			</v-data-table>
			<div class="Page2__header">
				<h1>This is where the output will be displayed!</h1>
			</div>
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
								<v-btn flat color="orange">Share</v-btn>
								<v-btn flat color="orange">Explore</v-btn>
							</v-card-actions>
						</v-card>
					</v-flex>
				</v-layout>
			</div>
	</div>
</template>

<script>

export default {
	data () {
      return {
        headers: [
          {
            text: 'Full Name',
            align: 'left',
            sortable: false,
            value: 'name'
          },
          { text: 'Address', value: 'address' },
          { text: 'Post Code', value: 'post-code' },
          { text: 'Company', value: 'company' },
          { text: 'Telephone Number', value: 'telephone-number' },
          { text: 'Email', value: 'email' }
        ],
        fields: []
      }
    }
}

</script>


<style lang="scss">
@import '../../settings';

.Page2 {
	
	&__header{
		padding: 2rem;
	}
}
</style>
