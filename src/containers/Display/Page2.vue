<template>
	<div class="Page2">
		<div class="Page2__results">
			<v-data-table
				:headers="headers"
				:items="fields"
				class="elevation-1"
				hide-actions>
				<template v-slot:items="props">
					<td>{{ props.item.first }}</td>
					<td>{{ props.item.last }}</td>
					<td>{{ props.item.email }}</td>
					<td>{{ props.item.address }}</td>
					<td>{{ props.item.phone }}</td>
					<td>{{ props.item.state }}</td>
					<td>{{ props.item.title }}</td>
				</template>
			</v-data-table>
		</div>
		<div class="Page2__header">
			<h2>Try again, save or view your data</h2>
		</div>
		<div class="Page2__buttons">
			<v-btn @click="exportData">Save</v-btn>
			<v-btn to="/">Try again</v-btn>
			<Store />	
		</div>		
	</div>
</template>

<script>
import Store from '../../components/Store.vue'
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
		Store
	},
	methods: {
		exportData(){
			this.$store.commit('addData', this.fields)
		}
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

	&__results {
		padding: 1rem;
	}

	&__card {
		padding: 1rem;
	}
	
	&__header {
		padding: 2rem;
	}

	&__buttons {
		padding: 1rem;
	}
}
</style>
