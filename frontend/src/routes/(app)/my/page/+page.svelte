<script lang="ts">
  import { writable } from "svelte/store";
  import { account } from "$lib/store";
  import { getResumesByMemberId, deleteResume } from "$lib/api/resume";
  import { getCommentsByMemberId, getCommentsByResumeId } from "$lib/api/comment";
  import type { Comment } from "$lib/interfaces/resume/Comment";
  import CommentView from "$lib/components/resume/CommentView.svelte";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import Button from "$lib/components/Button.svelte";
  import { goto } from "$app/navigation";
  import ResumeIcon from "$lib/icons/ResumeIcon.svelte";
  import FullListIcon from "$lib/icons/FullListIcon.svelte";
  import DeleteIconSmall from "$lib/icons/DeleteIconSmall.svelte";

  export const id = writable<number | null>(null);
  export const resumeId = writable<number | null>(null);

  let token: string | null = null;
  let memberComments: Comment[] = [];
  let resumes: {
    [id: string]: {
      resume: Resume;
      comments: Comment[];
    };
  } = {};

  const loadPage = async () => {
    if (!$account) return;
    token = sessionStorage.getItem("token");

    const resumesResponse = await getResumesByMemberId($account.id);

    memberComments = await getCommentsByMemberId($account.id);

    for (const resume of resumesResponse) {
      resumes[resume.id] = {
        resume,
        comments: await getCommentsByResumeId(resume.id)
      };
    }
  };

  function handleResumeDelete(resumeKey: string) {
    delete resumes[resumeKey];
    resumes = resumes;
    deleteResume(resumeKey);
  }

  $: if ($account) loadPage();
</script>

{#if $account}
  <section class="text-ce flex flex-col gap-5">
    <h1>Dashboard</h1>
    <div class="flex gap-4">
      <Button on:click={() => goto("/my/resumes/new")} style="labeled-icon">
        <ResumeIcon />
        Add Resume
      </Button>
      <Button on:click={() => goto("/my/resumes")} style="labeled-icon">
        <FullListIcon />
        Full list
      </Button>
    </div>
    <div>
      <h2>User Info</h2>
      <div class="mb-2 rounded-xl border-2 bg-white p-2">
        <p><strong>Email: </strong>{$account.email}</p>
      </div>
      <div>
        <h2>Resumes</h2>
        <div class="mb-2 rounded-xl border-2 bg-white p-2">
          <div class="flex flex-col divide-y divide-black">
            {#if Object.keys(resumes).length}
              {#each Object.entries(resumes) as [resumeId, { resume, comments }] (resumeId)}
                <div class="grid auto-cols-auto grid-flow-col p-4">
                  <div>
                    <a href={`/my/resumes/${resumeId}`}>
                      <span class="text-xl hover:font-medium">
                        {resume.title}
                      </span>
                    </a>
                    <p><strong>Shared:</strong> {resume.is_shareable ? "Yes" : "No"}</p>
                    <p><strong>Comments:</strong> {comments.length}</p>
                  </div>
                  <div class="self-center justify-self-end">
                    <Button on:click={() => handleResumeDelete(resumeId)} style="delete">
                      <DeleteIconSmall />
                    </Button>
                  </div>
                </div>
              {/each}
            {:else}
              <p><strong>No Resumes</strong></p>
            {/if}
          </div>
        </div>
      </div>
      <div>
        <h2>Community</h2>
        <div class="mb-2 rounded-xl border-2 bg-white p-2">
          <h3>Your Comments</h3>
          <CommentView
            bind:value={memberComments}
            config={{ isReadyOnly: true, isResumeTitleHidden: false }}
          ></CommentView>
        </div>
      </div>
    </div>
  </section>
{/if}
