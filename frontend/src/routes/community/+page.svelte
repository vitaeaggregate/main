<script lang="ts">
	import RichTextComposer from "$lib/components/svelte-lexical/RichTextComposer.svelte";
	import type { Comment } from "svelte/types/compiler/interfaces";
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