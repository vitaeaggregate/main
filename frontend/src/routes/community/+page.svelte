<script lang="ts">
	import RichTextComposer from "$lib/components/svelte-lexical/RichTextComposer.svelte";
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

<section>
	<div class="container">
		<div class="flex justify-center">
			<div class="max-w-4xl rounded-lg border-2">
				<RichTextComposer></RichTextComposer>
			</div>
		</div>
	</div>
	<br/>
	<h2>Comments</h2>
	<div>
	{#each comments as comment}
	<p>{comment.description}</p>
	{/each}
	<p>There is text here</p>
</div>
	
</section>