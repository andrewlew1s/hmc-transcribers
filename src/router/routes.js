import landingRoutes from '../containers/Home';
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
