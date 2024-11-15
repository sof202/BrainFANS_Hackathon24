import { Octokit } from "https://esm.sh/octokit";

const octokit = new Octokit({});

async function getLinesChanged(owner, repo, pull_number) {
    try {
        const { data: files } = await octokit.rest.pulls.listFiles({
            owner,
            repo,
            pull_number,
        });

        const totalLinesChanged = files.reduce(
            (acc, file) => acc + file.changes,
            0,
        );

        console.log(
            `Total lines changed in PR #${pull_number}: **${totalLinesChanged}**`,
        );
    } catch (error) {
        console.error("Error fetching pull request data:", error);
    }
}

async function getUser(owner, repo, pull_number) {
    try {
        const { data: pullRequest } = await octokit.rest.pulls.get({
            owner,
            repo,
            pull_number,
        });
        console.log(pullRequest.user.login);
    } catch (error) {
        console.error("Error fetching pull request data:", error);
    }
}

// Example usage
getLinesChanged("ejh243", "BrainFANS", 248);
getUser("ejh243", "BrainFANS", 248);
