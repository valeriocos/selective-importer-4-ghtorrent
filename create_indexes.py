__author__ = 'valerio cosentino'

import database_manager as dbman


def main():
    dbman.execute_sql_statement("USE " + dbman.DATABASE)

    if dbman.check_table_exists("projects"):
        dbman.execute_sql_statement("ALTER TABLE projects ADD INDEX forked_from (forked_from)")
        dbman.execute_sql_statement("ALTER TABLE projects ADD INDEX deleted (deleted)")
        #execute_sql_statement("ALTER TABLE projects ADD UNIQUE INDEX name (name, owner_id)")
        #execute_sql_statement("ALTER TABLE projects ADD INDEX owner_id (owner_id)")

    if dbman.check_table_exists("issues"):
        dbman.execute_sql_statement("ALTER TABLE issues ADD INDEX repo_id (repo_id)")
        dbman.execute_sql_statement("ALTER TABLE issues ADD INDEX issue_id (issue_id)")
        #execute_sql_statement("ALTER TABLE issues ADD INDEX reporter_id (reporter_id)")
        #execute_sql_statement("ALTER TABLE issues ADD INDEX assignee_id (assignee_id)")
        #execute_sql_statement("ALTER TABLE issues ADD INDEX pull_request_id (pull_request_id)")

    if dbman.check_table_exists("issue_events"):
        dbman.execute_sql_statement("ALTER TABLE issue_events ADD INDEX issue_id (issue_id)")
        dbman.execute_sql_statement("ALTER TABLE issue_events ADD INDEX action (action)")
        #execute_sql_statement("ALTER TABLE issue_events ADD INDEX actor_id (actor_id)")

    if dbman.check_table_exists("issue_labels"):
        dbman.execute_sql_statement("ALTER TABLE issue_labels ADD INDEX label_id (label_id)")

    if dbman.check_table_exists("repo_labels"):
        dbman.execute_sql_statement("ALTER TABLE repo_labels ADD KEY repo_id (repo_id)")

    if dbman.check_table_exists("pull_requests"):
        dbman.execute_sql_statement("ALTER TABLE pull_requests ADD INDEX head_repo_id (head_repo_id)")
        dbman.execute_sql_statement("ALTER TABLE pull_requests ADD INDEX base_repo_id (base_repo_id)")
        #execute_sql_statement("ALTER TABLE pull_requests ADD INDEX merged (merged)")
        #execute_sql_statement("ALTER TABLE pull_requests ADD INDEX user_id (user_id)")
        #execute_sql_statement("ALTER TABLE pull_requests ADD INDEX head_commit_id (head_commit_id)")
        #execute_sql_statement("ALTER TABLE pull_requests ADD INDEX base_commit_id (base_commit_id)")
        #execute_sql_statement("ALTER TABLE pull_requests ADD INDEX idx_pullreq_id (pullreq_id)")
        #execute_sql_statement("ALTER TABLE pull_requests ADD UNIQUE INDEX pullreq_id (pullreq_id, base_repo_id)")

    if dbman.check_table_exists("pull_request_history"):
        dbman.execute_sql_statement("ALTER TABLE pull_request_history ADD INDEX pull_request_id (pull_request_id)")
        dbman.execute_sql_statement("ALTER TABLE pull_request_history ADD INDEX action (action)")
        dbman.execute_sql_statement("ALTER TABLE pull_request_history ADD INDEX actor_id (actor_id)")

    #if check_table_exists("users"):
        #execute_sql_statement("ALTER TABLE users ADD INDEX user_email (email)")
        #execute_sql_statement("ALTER TABLE users ADD UNIQUE INDEX login (login)")

    if dbman.check_table_exists("issue_comments"):
        dbman.execute_sql_statement("ALTER TABLE issue_comments ADD INDEX issue_id (issue_id)")
        #execute_sql_statement("ALTER TABLE issue_comments ADD INDEX user_id (user_id)")

    #if check_table_exists("watchers"):
        #execute_sql_statement("ALTER TABLE watchers ADD INDEX user_id (user_id)")

    if dbman.check_table_exists("repo_milestones"):
        dbman.execute_sql_statement("ALTER TABLE repo_milestones ADD KEY repo_id (repo_id)")

    if dbman.check_table_exists("pull_request_commits"):
        dbman.execute_sql_statement("ALTER TABLE pull_request_commits ADD INDEX commit_id (commit_id)")

    if dbman.check_table_exists("pull_request_comments"):
        dbman.execute_sql_statement("ALTER TABLE pull_request_comments ADD INDEX pull_request_id (pull_request_id)")
        #execute_sql_statement("ALTER TABLE pull_request_comments ADD INDEX user_id (user_id)")
        #execute_sql_statement("ALTER TABLE pull_request_comments ADD INDEX commit_id (commit_id)")

    #if check_table_exists("project_members"):
        #execute_sql_statement("ALTER TABLE project_members ADD INDEX user_id (user_id)")

    #if check_table_exists("project_commits"):
        #execute_sql_statement("ALTER TABLE project_commits ADD INDEX commit_id (commit_id)")

    #if check_table_exists("organization_members"):
        #execute_sql_statement("ALTER TABLE organization_members ADD INDEX user_id (user_id)")

    #if check_table_exists("forks"):
        #execute_sql_statement("ALTER TABLE forks ADD INDEX forked_from_id (forked_from_id)")
        #execute_sql_statement("ALTER TABLE forks ADD INDEX forked_project_id (forked_project_id)")

    #if check_table_exists("followers"):
        #execute_sql_statement("ALTER TABLE followers ADD INDEX follower_id (follower_id)")

    if dbman.check_table_exists("commits"):
        dbman.execute_sql_statement("ALTER TABLE commits ADD INDEX project_id (project_id)")
        #execute_sql_statement("ALTER TABLE commits ADD UNIQUE INDEX sha (sha)")
        #execute_sql_statement("ALTER TABLE commits ADD INDEX author_id (author_id)")
        #execute_sql_statement("ALTER TABLE commits ADD INDEX committer_id (committer_id)")

    #if check_table_exists("commit_parents"):
    #    execute_sql_statement("ALTER TABLE commit_parents ADD INDEX parent_id (parent_id)")

    if dbman.check_table_exists("commit_comments"):
        dbman.execute_sql_statement("ALTER TABLE commit_comments ADD INDEX commit_id (commit_id)")
        #execute_sql_statement("ALTER TABLE commit_comments ADD UNIQUE INDEX comment_id (comment_id)")
        #execute_sql_statement("ALTER TABLE commit_comments ADD INDEX user_id (user_id)")

    dbman.close_connection()


if __name__ == "__main__":
    main()