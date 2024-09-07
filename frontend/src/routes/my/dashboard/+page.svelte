<script lang="ts">
	import { goto } from "$app/navigation";
	import { writable } from "svelte/store";
	import { account, loadedResumes, checkAccountAndRedirect } from "$lib/store";
	import { getAllResumes } from "$lib/api/resume";
	import { deleteComment, getCommentsByMemberId, getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { deleteResume } from "$lib/api/resume";
	import type { Comment } from "$lib/interfaces/resume/Comment";
	import type { Resume } from "$lib/interfaces/resume/Resume"

	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null);
	let token: string | null = null;

	// let memberComments: Comment[] = [];
	let resumeDisplay:Resume[] = []

	const loadPage = async () => {
		token = sessionStorage.getItem("token");

		const resumes = await getAllResumes();
		resumeDisplay = [...resumes]
	};
	// function handleResumeClick(resumeId: number) {
	// 	goto(`/community/${resumeId}`);
	// }
	function handleCreateResumeClick() {
		goto('/my/resumes/new');
	}

	checkAccountAndRedirect(loadPage);
</script>

<section class="">
	<div class="bfb">
		<button on:click={handleCreateResumeClick}>Create Resume</button>
	</div>
	<div>
		{#each resumeDisplay as resume}
			<ul>
				<li>	
					<a href='/community/{resume.id}'>{resume.title}</a>		
				</li>
			</ul>
		{/each}
	</div>
</section>

<!-- <{#if $account}
	<section class="">
		<h1>Dashboard</h1>
		<div class="">
			<div>
				<h2>User Info</h2>
				<ul class="flex flex-col gap-5 p-5">
					<li class="rounded-lg border-2 p-2">
						<p><strong>Id: </strong>{$account.id}</p>
						<p><strong>Token: </strong>{token}</p>
						<p><strong>Email: </strong>{$account.email}</p>
					</li>
				</ul>
			</div>
			<div>
				<h2 class="mb-3"><a href="/my/resumes">Resumes</a></h2>
				<a href="/my/resumes/new">Add Resume</a>
				{#if Object.keys($loadedResumes).length}
					<ul class="flex flex-col gap-5 p-5">
						{#each Object.entries($loadedResumes).reverse() as [resumeId, { resume, comments }]}
							<li class="rounded-lg border-2 p-2">
								<p><span class="text-xl">{resume.title}</span></p>
								<p><strong>Resume id:</strong> {resume.id}</p>
								<p class="hover:italic">
									<a href={`/community/${resumeId}`}><strong>Title:</strong> {resume.title}</a>
								</p>
								<p><strong>Shared:</strong> {resume.is_shareable ? "Yes" : "No"}</p>
								<h3>Comments</h3>
								{#if Object.keys(comments).length}
									<ul class="flex flex-col gap-5 p-5">
										{#each Object.entries(comments) as [commentId, comment]}
											<li class="rounded-lg border-2 p-2">
												<p><strong>Member id:</strong> {comment.member}</p>
												<p><strong>Comment:</strong> {comment.description}</p>
												<button
												on:click={() => {
													handleDeleteComment($account.id, resume.id, comment.id);
												}}>Delete</button
											>
											</li>
										{/each}
									</ul>
								{:else}
									<p><strong>No Comments</strong></p>
								{/if}
								<button
									on:click={() => {
										handleDelete($account.id, resume.id);
									}}>Delete Resume</button
								>
							</li>
						{/each}
					</ul>
				{:else}
					<p><strong>No Resumes</strong></p>
				{/if}
			</div>
			<div>
				<h2>Community</h2>
				<h3>Your Comments</h3>
				{#if memberComments.length}
					<ul class="flex flex-col gap-5 p-5">
						{#each memberComments as comment}
							<li class="rounded-lg border-2 p-2">
								<p><strong>Resume id:</strong> {comment.header}</p>
								<p><strong>Comment:</strong> {comment.description}</p>
							</li>
						{/each}
					</ul>
				{:else}
					<p><strong>No Comments</strong></p>
				{/if}
			</div>
		</div>
	</section>
{/if}> -->
