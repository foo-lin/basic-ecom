<template>
	<div class="homepage">
		<div class="header">
			<transition name="el-fade-in-linear">
				<div class="hero" v-show="show">
					<h1>Fansui Fish</h1>
					<h2>Lowest Price in the Market</h2>
					<h3>Updated Stock every week</h3>
					<el-button type="primary">Shop Now</el-button>
				</div>
			</transition>
		</div>
		<main class="main" id="main">
			<section class="category section-padding" id="category">
				<div :class="['item', `item__${i}`]" v-for="i in 6" :key="i">
					{{ i }}
				</div>
			</section>
			<section class="top section-padding" id="top">
				<el-carousel :interval="4000" type="card" height="500px">
					<el-carousel-item v-for="item in 6" :key="item">
						<h3 class="medium">{{ item }}</h3>
					</el-carousel-item>
				</el-carousel>
			</section>

			<section class="reviews section-padding" id="reviews">
				<el-carousel
					height="90vh"
					direction="vertical"
					:autoplay="true"
				>
					<el-carousel-item v-for="item in 4" :key="item">
						<h3 class="medium">{{ item }}</h3>
					</el-carousel-item>
				</el-carousel>
			</section>

			<section class="contact section-padding" id="contact">
				<div class="contact-container" id="df">
					<div class="contact-form">
						<div class="form-heading">
							<h2 class="heading-2">Contact Us</h2>
						</div>
						<form class="form">
							<el-input
								placeholder="Please input"
								v-model="input"
								clearable
								prefix-icon="el-icon-user"
							>
							</el-input>
							<el-input
								placeholder="Please input"
								v-model="input"
								clearable
								prefix-icon="el-icon-message
"
							>
							</el-input>
							<el-input
								type="textarea"
								:rows="4"
								placeholder="Please input"
								v-model="textarea"
							>
							</el-input>

							<el-button type="submit">Submit</el-button>
						</form>
					</div>
				</div>
			</section>
		</main>
	</div>
</template>

<script>
export default {
	name: "homepage",
	data() {
		return {
			show: true,
			input: "dsf"
		};
	}
};
</script>

<style lang="scss" scoped>
.homepage {
	.section-padding {
		padding: 4rem 0;
	}
	.header {
		height: 100vh;
		background-image: linear-gradient(
				to right bottom,
				rgba(0, 0, 0, 0.8),
				rgba(255, 255, 255, 0.2)
			),
			url(https://images.unsplash.com/photo-1578507065211-1c4e99a5fd24?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80);
		background-size: cover;
		background-position: center;
		position: relative;
		.hero {
			position: absolute;
			top: 40%;
			left: 10%;
			text-align: center;
			line-height: 5rem;
			color: grey;

			h1 {
				font-size: 50px;
			}
			h2 {
				font-size: 30px;
			}
			h3 {
				font-size: 26px;
			}
		}
	}
	.main {
		padding: 0 5rem;
	}

	.category {
		display: grid;
		grid-template-columns: repeat(6, 1fr);
		grid-template-rows: repeat(6, 1fr);
		grid-gap: 2rem;
		height: 100vh;
	}

	.item {
		background: red;
		&__1 {
			grid-row: 1 / span 3;
			grid-column: 1 / span 4;
		}
		&__2 {
			grid-row: 1 / span 3;
			grid-column: 5 / span 2;
		}
		&__3 {
			grid-row: 4 / span 2;
			grid-column: 1 / span 2;
		}
		&__4 {
			grid-row: 4 / span 2;
			grid-column: 3 / span 2;
		}
		&__4 {
			grid-row: 4 / span 2;
			grid-column: 3 / span 2;
		}
		&__5 {
			grid-row: 4 / span 2;
			grid-column: 5 / span 2;
		}
		&__6 {
			grid-row: 6 / span 1;
			grid-column: 1 / -1;
		}
	}

	.top {
		.el-carousel__item:nth-child(2n) {
			background-color: #99a9bf;
		}

		.el-carousel__item:nth-child(2n + 1) {
			background-color: #d3dce6;
		}
	}
	.reviews {
		.el-carousel__item:nth-child(2n) {
			background-color: #99a9bf;
		}

		.el-carousel__item:nth-child(2n + 1) {
			background-color: #d3dce6;
		}
	}

	.contact {
		&-container {
			height: 70vh;
			width: 90%;
			margin: 0 auto;
			background-image: linear-gradient(
					105deg,
					rgba(white, 0.9) 0%,
					rgba(white, 0.9) 50%,
					transparent 50%
				),
				url(https://images.unsplash.com/photo-1578507065211-1c4e99a5fd24?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80);
			background-attachment: fixed;
			background-position: center;
			background-repeat: no-repeat;
			background-size: cover;
			border-radius: 10px;
		}
		&-form {
			width: 45%;
			padding: 3rem;
		}
		.form-heading {
			text-align: center;
			margin: 2rem 0;
			font-size: 3rem;
			color: #03a9f4;
		}

		.form {
			& > * {
				margin-bottom: 4rem;
			}
		}
	}
}
</style>
