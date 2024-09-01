<script>
	import RichTextComposer from "../../lib/svelte-lexical/src/RichTextComposer.svelte";
	import "../../lib/svelte-lexical/src/global.css";
</script>

<main>
	<h1>Community</h1>
	<p>
		Welcome to <a href="https://github.com/umaranis/svelte-lexical/"> svelte-lexical </a>
		demo built using
		<a href="https://kit.svelte.dev">SvelteKit</a>
	</p>
	<div style="text-align: left;">
		<RichTextComposer />
	</div>
</main>

<style>
	main {
		padding: 1em;
		max-width: none;
		margin: 0 auto;
	}
</style>
