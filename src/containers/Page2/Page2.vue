<template>
	<div class="Page2">
			<div class="Page2__header">
				<!-- <h1>{{data}}</h1> -->
			</div>
			<v-data-table
				:headers="headers"
				:items="fields"
				class="elevation-1">
				<template v-slot:items="props">
					<!-- <td>{{ props.item.name }}</td> -->
					<td>{{ props.item.first }}</td>
					<td>{{ props.item.last }}</td>
					<td>{{ props.item.email }}</td>
					<td>{{ props.item.address }}</td>
					<td>{{ props.item.phone }}</td>
					<td>{{ props.item.state }}</td>
					<td>{{ props.item.title }}</td>
				</template>
			</v-data-table>
			<div class="Page2__header">
				<h2>Or try again with another card:</h2>
			</div>
			<Browse />
	</div>
</template>

<script>
import Browse from '../../components/Browse.vue'
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
	components: {
		Browse
	},

	computed: {
		...mapState([
			'data'
		])
	}
}
</script>

<style lang="scss">
@import '../../settings';

.Page2 {

	&__card {
		padding: 1rem;
	}
	
	&__header{
		padding: 2rem;
	}
}
</style>
