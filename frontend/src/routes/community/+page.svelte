<script lang="ts">
	import RichTextComposer from "$lib/components/svelte-lexical/RichTextComposer.svelte";
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import { error } from "@sveltejs/kit";
	import { account } from "$lib/store";
	import { resume } from "$lib/store";
  	import { onMount } from "svelte";
	import { PUBLIC_SERVER } from "$env/static/public";
	import { writable } from "svelte/store";
	import { fetchData } from "$lib/utils";

	export const id = writable<number | null>(null);
  let comments: Comment[] = [];

  onMount(async () => {
	// if (!$account) return goto("/login/test");
	const requestInit: RequestInit = {
			method: "GET"
		};
const response = await fetchData(`${PUBLIC_SERVER}/members/${$account.id}/resumes/${$resume.id}/comments`, requestInit);

if (!response.ok) {
			return error(response.status, response.statusText);
		}


const commentsData: Comment[] = await response.json();
comments = commentsData;
console.log(comments)
  });

</script>

<!-- <section>
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
	
</section> -->
<main>
<h1>Community</h1>
<br/>
<div class="flex justify-center">

<div class="w-4/5 h-3/5 bg-gray-200 overflow-y-auto p-6">
	  /// this is the main content div that i need the content inside to scroll internally
	  /// what i mean by this is i dont want the whole page to move when there is a lot of content 
	  /// just the content inside this divdddddddddddddddddddddddddddddddddddddddddddddddddddddd
</div>
	</div>
	<br />
	<h2>Comments</h2>
	<div>{comments.description}</div>
	
</main>