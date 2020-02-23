<template>
	<div class="body">
		<navbar></navbar>
		<router-view></router-view>
	</div>
</template>

<script>
import Navbar from "./components/Navbar";

export default {
	name: "App",
	components: {
		Navbar
	}
};
</script>

<style>
*,
*::before,
*::after {
	padding: 0;
	margin: 0;
}
body {
	position: relative;
}
</style>
