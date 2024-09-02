<script lang="ts">
	import RichTextComposer from "../../lib/svelte-lexical/src/RichTextComposer.svelte";
	import "../../lib/svelte-lexical/src/global.css";
	import type { Comment } from "svelte/types/compiler/interfaces";

  import { onMount } from "svelte";

  let comments: Comment[] = [];

  onMount(async () => {
	const url = "http://localhost:8000/members/1/resumes/1/comments"; // Construct URL with API endpoint

const response = await fetch(url);
const commentsData: Comment[] = await response.json();
comments = commentsData;
console.log(comments)
  });

</script>

<div class="p-2 m-auto">
	<h1>Community</h1>
	<p>
		Welcome to <a href="https://github.com/umaranis/svelte-lexical/"> svelte-lexical </a>
		demo built using
		<a href="https://kit.svelte.dev">SvelteKit</a>
	</p>
	<div style="text-align: left;">
		<RichTextComposer />
	</div>
	<br/>
	<h2>Comments</h2>
	<div>
	{#each comments as comment}
	<p>{comment.description}</p>
	{/each}
	<p>There is text here</p>
</div></div>
	
