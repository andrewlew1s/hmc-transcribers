import landingRoutes from '../containers/Page1';
import displayRoutes from '../containers/Display';
import aboutRoutes from '../containers/About';

const routes = [
	...landingRoutes,
	...displayRoutes,
	...aboutRoutes,
	{
		path: '*',
		redirect: '/'
	}
];

export default routes;
