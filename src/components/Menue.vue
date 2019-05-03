<template>
	<div class="Menue">
		<b-link
			class="Menue__link"
			v-for="item in menuItems"
			:key="item.path"
			:to="item.path"
			exact
			v-text="item.name"/>

	</div>
</template>

<script>
/* Component to render a styled menu.

	Properties:
		- Items: An array of menu item obejcts:
		{ path: '/butts', name:'Click me' }

		- Auto: if set to true will automatically display
		from the routes.js file with the property `menu`
		set to `true`.

 */
import routes from '../router/routes';

export default {
	props: [
		'auto',
		'items'
	],
	data() {
		return {
			routes
		};
	},
	computed: {
		menuItems() {
			if (this.auto) {
				return this.routes.filter(route => route.menu);
			}
			return this.items;
		}
	}
};

</script>

<style lang="scss">
@import '../settings';

.Menue{

	text-align: center;
	border-bottom: 1px solid $Grey;

		&__link{
			font-size: 20px;
			border-bottom: 1px solid $Grey;
			color: $Text_Colour !important;
			text-decoration: none !important;
			padding-bottom: 0.2em;
			margin: 10px 20px;
			display: inline-block;
			text-decoration: none;
			transition: 50ms;

			@media all and (max-width: $Mobile_Width){
				font-size: 12px;
				margin: 5px 8px;
			}

			&.active, &:hover{
				border-bottom: 2px solid $Text_Colour;
			}

			&:active{
				position: relative;
				top: 2px;
			}
		}
	}
	
</style>
