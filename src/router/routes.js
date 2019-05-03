import landingRoutes from '../containers/Page1';
import page2Routes from '../containers/Page2';
import aboutRoutes from '../containers/About';

const routes = [
	...landingRoutes,
	...page2Routes,
	...aboutRoutes,
	{
		path: '*',
		redirect: '/'
	}
];

export default routes;
