<template>
	<div class="homepage">
		<div class="header"></div>
	</div>
</template>

<script>
export default {
	name: "homepage"
};
</script>

<style lang="scss" scoped>
.header {
	width: 100vw;
	height: 95vh;
	background-image: linear-gradient(
			to right bottom,
			rgba(255, 255, 255, 0.1),
			rgba(255, 255, 255, 0.2)
		),
		url(https://images.unsplash.com/photo-1578507065211-1c4e99a5fd24?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80);
	background-size: cover;
	background-position: center;
}
</style>
