<script lang="ts">
	import { goto } from "$app/navigation";
	import { getCommentsByMemberIdByResumeId } from "$lib/api/comment";
	import { getResumesByMemberId } from "$lib/api/resume";
	import { account, isAuthenticated, loadedResumes } from "$lib/store";

	$: {
		if (!$isAuthenticated) goto("/login/test");
		if ($account) loadPage();
	}

	const loadPage = async () => {
		if (!$account) return;

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
</script>

<section>
	<h1>My Resumes</h1>
	{#if $account}
		<div>
			{#if Object.keys($loadedResumes).length}
				<ul class="flex flex-col gap-5 p-5">
					{#each Object.entries($loadedResumes) as [resumeId, { resume, comments }]}
						<li class="rounded-lg border-2 p-2">
							<h2>{resume.title}</h2>
							<hr class="my-3" />
							<p><strong>Resume Id:</strong> {resumeId}</p>
							<p><strong>Created at:</strong> {new Date(resume.created_at).toLocaleDateString()}</p>
							<p><strong>Updated at:</strong> {new Date(resume.created_at).toLocaleDateString()}</p>
							<hr class="my-3" />
							<h3>Comments:</h3>
							{#if Object.keys(comments).length}
								<ul class="flex flex-col gap-5 p-5">
									{#each Object.entries(comments) as [commentId, comment]}
										<li class="rounded-lg border-2 p-2">
											<p><strong>Comment Id:</strong> {commentId}</p>
											<p><strong>Comment:</strong> {comment.description}</p>
										</li>
									{/each}
								</ul>
							{:else}
								<p><strong>Nothing here.</strong></p>
							{/if}
						</li>
					{/each}
				</ul>
			{:else}
				<p><strong>So Empty...</strong></p>
			{/if}
		</div>
	{/if}
</section>
