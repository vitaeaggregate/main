<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import { account } from "$lib/store";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { getCommentsByMemberId, getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import type { Resume } from "$lib/interfaces/resume/Resume";
	import type Comment from "$lib/interfaces/resume/Comment";

	export const id = writable<number | null>(null);

	type ResumesComments = {};

	let resumes: Resume[] | null = null;
	let memberComments: Comment[] | null = null;
	let resumesComments: { [resumeId: number]: Comment[] } = {};

	onMount(async () => {
		if (!$account) return goto("/login/test");

		resumes = await getResumesByMemberId($account.id);
		memberComments = await getCommentsByMemberId($account.id);

		if (!resumes) return;

		for (let resume of resumes) {
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			resumesComments[resume.id] = comments;
		}
	});
</script>

<section class="">
	{#if $account}
		<div><h1>Dashboard</h1></div>
		<div>
			<div>
				<h2>Member Info</h2>
				<ul class="flex flex-col gap-5 p-5">
					<li class="rounded-lg border-2 p-2">
						<p><strong>Id: </strong>{$account.id}</p>
						<p><strong>Email: </strong>{$account.email}</p>
					</li>
				</ul>
			</div>
			<div>
				<h2><a href="/my/resumes">Resumes</a></h2>
				{#if resumes}
					<ul class="flex flex-col gap-5 p-5">
						{#each resumes as resume}
							<li class="rounded-lg border-2 p-2">
								<p><strong>Resume id:</strong> {resume.id}</p>
								<p><strong>Title:</strong> {resume.title}</p>
								<h3>Comments</h3>
								<ul class="flex flex-col gap-5 p-5">
									{#if resumesComments[resume.id]?.length}
										{#each resumesComments[resume.id] as comment}
											<li class="rounded-lg border-2 p-2">
												<p><strong>Member id:</strong> {comment.member}</p>
												<p><strong>Comment:</strong> {comment.description}</p>
											</li>
										{/each}
									{:else}
										<li class="rounded-lg border-2 p-2">
											<p><strong>No Comments</strong></p>
										</li>
									{/if}
								</ul>
							</li>
						{/each}
					</ul>
				{:else}
					<p>No Resumes</p>
				{/if}
			</div>
			<div>
				<h2>Community</h2>
				<h3>Your Comments</h3>
				{#if memberComments}
					<ul class="flex flex-col gap-5 p-5">
						{#each memberComments as comment}
							<li class="rounded-lg border-2 p-2">
								<p><strong>Resume id:</strong> {comment.header}</p>
								<p><strong>Comment:</strong> {comment.description}</p>
							</li>
						{/each}
					</ul>
				{:else}
					<p>No Comments</p>
				{/if}
			</div>
		</div>
	{/if}
</section>
