<script lang="ts">
	import { goto } from "$app/navigation";
	import type CommentNotification from "$lib/interfaces/member/CommentNotification";
	import TimeAgo from "javascript-time-ago";
	import en from "javascript-time-ago/locale/en";
	import Button from "$lib/components/Button.svelte";
	import { onMount } from "svelte";
	import { dismissNotification } from "$lib/api/commentNotification";
	import { account, commentNotifications } from "$lib/store";

	export let value: CommentNotification[];

	TimeAgo.addDefaultLocale(en);

	const handleDismissClick = (notificationId: number) => {
		if (!$account) return;
		value = value.filter((notification) => notification.id !== notificationId);
		dismissNotification($account.id, notificationId);
	};
</script>

{#if value}
	<div class="flex flex-col-reverse gap-4">
		{#each value as commentNotification (commentNotification.id)}
			<div class="rounded-lg border-2 p-4">
				<div>
					<p><strong>Id: </strong>{commentNotification.id}</p>
					<p>
						<strong>Resume Id: </strong>{commentNotification.header.id}
					</p>
					<p>
						<a href={"/community/" + commentNotification.header.id}
							><strong>Resume Title: </strong>{commentNotification.header.title}</a
						>
					</p>
					<p><strong>Comment: </strong>{commentNotification.comment.description}</p>
					<p>
						<strong>Created: </strong>{new TimeAgo("en-US").format(
							new Date(commentNotification.created_at)
						)}
					</p>
				</div>
				<Button on:click={() => handleDismissClick(commentNotification.id)}>Dismiss</Button>
			</div>
		{/each}
	</div>
{/if}
