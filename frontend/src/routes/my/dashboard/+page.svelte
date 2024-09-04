<script lang="ts">
	import { account, checkAccountAndRedirect, loadedResumes } from "$lib/store";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { getCommentsByMemberId, getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { deleteResume } from "$lib/api/resume";
	import type { Comment } from "$lib/interfaces/resume/Comment";

	let token: string | null = null;

	let memberComments: Comment[] = [];

	const loadPage = async () => {
		if (!$account) return;

		token = sessionStorage.getItem("token");

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

		console.log(memberComments)

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

	function handleDelete(id: number, resumeId: number) {
		deleteResume(id, resumeId);
		delete $loadedResumes[id];
	}

	checkAccountAndRedirect(loadPage);
</script>

{#if $account}
	<section class="">
		<h1>Dashboard</h1>
		<div>
			<div>
				<h2>Member Info</h2>
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
								<p><strong>Shared:</strong> {resume.is_shareable ? "Yes" : "No"}</p>
								<h3>Comments</h3>
								{#if Object.keys(comments).length}
									<ul class="flex flex-col gap-5 p-5">
										{#each Object.entries(comments) as [commentId, comment]}
											<li class="rounded-lg border-2 p-2">
												<p><strong>Member id:</strong> {comment.member}</p>
												<p><strong>Comment:</strong> {comment.description}</p>
											</li>
										{/each}
									</ul>
								{:else}
									<p><strong>No Comments</strong></p>
								{/if}
								<button
									on:click={() => {
										handleDelete($account.id, resume.id);
									}}>Delete</button
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
{/if}
