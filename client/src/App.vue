<template>
	<div class="body">
		<navbar></navbar>
		<router-view></router-view>
		<Footer></Footer>
	</div>
</template>

<script>
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

export default {
	name: "App",
	components: {
		Navbar,
		Footer
	}
};
</script>

<style>
*,
*::before,
*::after {
	padding: 0;
	margin: 0;
	box-sizing: border-box !important;
}
body {
	position: relative;
}
html {
	font-size: 62.5%;
}
</style>
