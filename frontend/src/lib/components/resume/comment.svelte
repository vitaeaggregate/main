<script lang="ts">
	import { createComment } from "$lib/api/comment";
    import type { BaseComment, Comment } from "$lib/interfaces/resume/Comment";
	import { account } from "$lib/store";

    
	export const id: number | null = null;

async function handleCreate() {
    if (!$account) return;

    const commentObject: BaseComment = {

    }

    await createComment($account.id, commentObject)
}

</script>
<div>
<button on:click={handleCreate}>Submit</button>
</div>