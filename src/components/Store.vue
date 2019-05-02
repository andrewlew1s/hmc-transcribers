<template>
	<div class="Store">
			<div class="Store__header">
				<!-- <h1>{{data}}</h1> -->
			</div>
      <li v-for="item in this.$store.state.data" v-bind:key="item.first">
        {{item}}
      </li>
	</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
	data () {
      return {
        headers: [
			{ text: 'First Name', value: 'first' },
			{ text: 'Last Name', value: 'last' },
			{ text: 'Email', value: 'email' },     
			{ text: 'Address', value: 'address' },
			{ text: 'Phone', value: 'phone' },
			{ text: 'State', value: 'state' },
			{ text: 'Title', value: 'title' },
        ],
        fields: [
			{
				first: this.$store.state.data.first,
				last: this.$store.state.data.last,
				email: this.$store.state.data.email,
				address: this.$store.state.data.address,
				phone: this.$store.state.data.phone,
				state: this.$store.state.data.state,
				title: this.$store.state.data.title
			}
		]
      }
		},
	methods: {
		
	},

	computed: {
		...mapState([
			'data'
		])
	}
}
</script>

<style lang="scss">

.Store {

	&__card {
		padding: 1rem;
	}
	
	&__header{
		padding: 2rem;
	}
}
</style>