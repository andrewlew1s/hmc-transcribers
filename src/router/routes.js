import landingRoutes from '../containers/Page1';
import page2Routes from '../containers/Page2';

const routes = [
	...landingRoutes,
	...page2Routes,
	
	{
		path: '*',
		redirect: '/'
	}
];

export default routes;
