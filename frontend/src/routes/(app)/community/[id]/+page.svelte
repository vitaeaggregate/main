<script lang="ts">
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import { createComment, deleteComment, getCommentsByResumeId } from "$lib/api/comment";
  import { getResumeById } from "$lib/api/resume";
  import { account } from "$lib/store";
  import { page } from "$app/stores";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { goto } from "$app/navigation";
  import Button from "$lib/components/Button.svelte";
  import CommentView from "$lib/components/resume/CommentView.svelte";
  import ResumePreview from "$lib/components/resume/ResumePreview.svelte";
  import OnigiriIcon from "$lib/icons/OnigiriIcon.svelte";

  let resumePromise: Promise<Resume>;
  let resumeComments: Comment[] = [];
  let newComment: Comment = {
    description: ""
  };

  let resumeElement: HTMLElement | null = null;
  let previewContainer: HTMLDivElement | null = null;
  let previewContainerWidth: number;
  let resumeElementSize: {
    height: number;
    width: number;
  } = {
    height: 0,
    width: 0
  };

  const loadPage = async () => {
    resumePromise = getResumeById($page.params.id).then(async (resume) => {
      resumeComments = await getCommentsByResumeId($page.params.id);
      return resume;
    });
  };

  const handleGoBack = () => goto("/community");

  const handleNewComment = async () => {
    if (!$account) return;
    newComment.member = $account.id;
    newComment.header = $page.params.id;
    const comment = await createComment(newComment);
    resumeComments.push(comment);
    resumeComments = resumeComments;
    newComment = {};
  };

  $: {
    if (previewContainer && previewContainerWidth && resumeElement && resumeElementSize) {
      const scale = previewContainerWidth / resumeElementSize.width;
      resumeElement.style.transform = `scale(${scale})`;
      const currentHeight = Math.round(resumeElementSize.height * scale);
      previewContainer.style.height = currentHeight + "px";
    }
  }

  $: if ($page.params.id && $account) loadPage();
</script>

{#if $account}
  <section class="flex h-full flex-col gap-5">
    {#await resumePromise then resume}
      <div class="flex gap-5">
        <Button on:click={handleGoBack} style="cancel">Back</Button>
        <h1>Community</h1>
      </div>
      <div class="rounded-lg bg-slate-100 p-5 shadow-lg">
        <div bind:this={previewContainer} bind:clientWidth={previewContainerWidth}>
          <ResumePreview {resume} bind:resumeElement bind:resumeElementSize></ResumePreview>
        </div>
      </div>
      <div class="flex flex-col">
        <h2>Comments</h2>
        <CommentView
          bind:value={resumeComments}
          config={{ isReadyOnly: true, isResumeTitleHidden: true }}
        ></CommentView>
      </div>
      <div class="flex flex-col gap-3">
        <h2>New Comment</h2>
        <CommentView
          bind:value={newComment}
          config={{ isReadyOnly: false, isResumeTitleHidden: true }}
        ></CommentView>
        <Button on:click={handleNewComment} style="submit">Send</Button>
      </div>
    {:catch}
      <div class="flex grow flex-col items-center justify-center text-center">
        <div class="absolute -z-10 size-60 opacity-10">
          <OnigiriIcon></OnigiriIcon>
        </div>
        <h1>404</h1>
        <h2>Onigiri not found or is not shared.</h2>
      </div>
    {/await}
  </section>
{/if}
