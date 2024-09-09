<script lang="ts">
	export let label: string = "Input Date";
	export let value: Date | undefined | string;
</script>

<label class="flex flex-col">
	{label}:
	<input type="date" bind:value class="border-2" />
</label>
