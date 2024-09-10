<script lang="ts">
	import { writable } from "svelte/store";
	import { account, loadedResumes, checkAccountAndRedirect } from "$lib/store";
	import { getResumesByMemberId } from "$lib/api/resume";
	import {
		deleteComment,
		getCommentsByMemberId,
		getCommentsByMemberIdByResumeId
	} from "$lib/api/comment";
	import { deleteResume } from "$lib/api/resume";
	import type { Comment } from "$lib/interfaces/resume/Comment";

	export const id = writable<number | null>(null);
	export const resumeId = writable<number | null>(null);
	let token: string | null = null;
	let email: string | null = null;

	let memberComments: Comment[] = [];

	const loadPage = async () => {
		if (!$account) return;

		token = sessionStorage.getItem("token");
		email = $account.email;

		const resumes = await getResumesByMemberId($account.id);

		loadedResumes.update((current) => {
			resumes.forEach((resume) => {
				current[resume.id] = {
					resume,
					comments: {}
				};
			});
			return current;
		});

		memberComments = await getCommentsByMemberId($account.id);

		for (const resume of resumes) {
			const comments = await getCommentsByMemberIdByResumeId($account.id, resume.id);
			loadedResumes.update((current) => {
				for (const comment of comments) {
					current[resume.id].comments[comment.id] = comment;
				}
				return current;
			});
		}
	};

	function handleResumeDelete(id: number, resumeId: number) {
		deleteResume(id, resumeId);
		delete $loadedResumes[id];
	}

	function handleDeleteComment(id: number, resumeId: number, commentId: number) {
		deleteComment(id, resumeId, commentId);
	}

	checkAccountAndRedirect(loadPage);
</script>

{#if $account}
	<section class="">
		<h1>Dashboard</h1>
		<div class="">
			<div>
				<h2>User Info</h2>
				<div class="border-2 bg-slate-200 p-2 mb-2">
				<ul class="flex flex-col gap-5 p-5">
					<li class="v-screen overflow-x-auto rounded-lg border-2 p-2">
						<p><strong>Id: </strong>{$account.id}</p>
						<p class="break-all"><strong>Token: </strong>{token}</p>
						{#if email}
							<p><strong>Email: </strong>{email}</p>
						{:else}
							<p><strong>Email: </strong>{$account.email}</p>
						{/if}
					</li>
				</ul>
			</div>
			</div>
			<div>
				<h2>Resumes</h2>
				<div class="border-2 bg-slate-200 p-2 mb-2">
				<a href="/my/resumes/new">Add Resume</a> || <a href="/my/resumes">Full list</a>
				{#if Object.keys($loadedResumes).length}
					<ul class="flex flex-col gap-5 p-5">
						{#each Object.entries($loadedResumes).reverse() as [resumeId, { resume, comments }]}
							<li class="rounded-lg border-2 p-2">
								<p><span class="text-xl hover:font-medium"><a href={`/my/resumes/${resumeId}`}>{resume.title}</a></span></p>
								<p><strong>Resume id:</strong> {resume.id}</p>
								<!-- <p><strong>Title:</strong> {resume.title}
								</p> -->
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
							</li>
						{/each}
					</ul>
				{:else}
					<p><strong>No Resumes</strong></p>
				{/if}
			</div>
		</div>
			<div>
				<h2>Community</h2>
				<div class="border-2 bg-slate-200 p-2 mb-2">
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
					<p class="p-5"><strong>No Comments</strong></p>
				{/if}
			</div>
		</div>
	</div>
	</section>
{/if}
