import { Octokit } from "https://esm.sh/octokit";

const octokit = new Octokit({});

async function getPullRequestsSinceDate(owner, repo, sinceDate) {
    try {
        const { data: pullRequests } = await octokit.rest.pulls.list({
            owner,
            repo,
            state: "all",
        });

        const filteredPRs = pullRequests.filter((pr) =>
            new Date(pr.created_at) > new Date(sinceDate)
        );

        const pullRequestNumbers = filteredPRs.map((pr) => pr.number);

        return pullRequestNumbers;
    } catch (error) {
        console.error(error);
    }
}

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

        return totalLinesChanged;
    } catch (error) {
        console.error("Error fetching pull request data:", error);
    }
}

async function getUsers(owner, repo, pull_number) {
    try {
        const { data: commits } = await octokit.rest.pulls.listCommits({
            owner,
            repo,
            pull_number,
        });
        const users = commits.map((commit) => commit.author.login);
        const uniqueUsers = [...new Set(users)];
        return uniqueUsers;
    } catch (error) {
        console.error("Error fetching pull request data:", error);
    }
}

async function getCommits(owner, repo, pull_number) {
    try {
        const { data: commits } = await octokit.rest.pulls.listCommits({
            owner,
            repo,
            pull_number,
        });
        return (commits.length);
    } catch (error) {
        console.error("Error fetching pull request data:", error);
    }
}

function getTeam(user) {
    const teamOne = ["sof202", "marinafloresp", "siyiSEA"];
    const teamTwo = ["ew267", "alicemfr", "rhaigh5"];
    let team = 0;
    if (teamOne.includes(user)) {
        team = 1;
    } else if (teamTwo.includes(user)) {
        team = 2;
    }
    return team;
}
