import type { BaseResume } from "$lib/interfaces/resume/Resume";

export type BaseResumeTypes<ignoreArray extends boolean = false> = {
	[key in keyof BaseResume]: BaseResume[key] extends Array<infer InnerType>
		? ignoreArray extends true
			? InnerType
			: BaseResume[key] | InnerType
		: never;
}[keyof BaseResume];