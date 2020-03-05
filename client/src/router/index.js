import Vue from "vue";
import VueRouter from "vue-router";
import Homepage from "../views/Homepage";
import Shoppage from "../views/Shop";
Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		component: Homepage,
		name: "homepage"
	},
	{
		path: "/shop",
		component: Shoppage,
		name: "shoppage"
	}
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes
});

export default router;
