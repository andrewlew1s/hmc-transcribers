import landingRoutes from '../containers/Page1';
import page2Routes from '../containers/Page2';
import page3Routes from '../containers/Page3';


const routes = [
	...landingRoutes,
	...page2Routes,
	...page3Routes,
	{
		path: '*',
		redirect: '/'
	}
];

export default routes;
