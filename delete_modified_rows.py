__author__ = 'valerio cosentino'

import database_manager as dbman


#delete useless rows (id = -1)
def main():
    dbman.execute_sql_statement("USE " + dbman.DATABASE)

    if dbman.check_table_exists('projects'):
        dbman.execute_sql_statement("DELETE FROM projects WHERE id = -1")

    if dbman.check_table_exists('issues'):
        dbman.execute_sql_statement("DELETE FROM issues WHERE id = -1")

    if dbman.check_table_exists('commits'):
        dbman.execute_sql_statement("DELETE FROM commits WHERE id = -1")

    if dbman.check_table_exists('commit_comments'):
        dbman.execute_sql_statement("DELETE FROM commit_comments WHERE id = -1")

    if dbman.check_table_exists('commit_parents'):
        dbman.execute_sql_statement("DELETE FROM commit_parents WHERE commit_id = -1 AND parent_id = -1")

    if dbman.check_table_exists('project_members'):
        dbman.execute_sql_statement("DELETE FROM project_members WHERE repo_id = -1 AND user_id = -1")

    if dbman.check_table_exists('watchers'):
        dbman.execute_sql_statement("DELETE FROM watchers WHERE repo_id = -1 AND user_id = -1")

    if dbman.check_table_exists('forks'):
        dbman.execute_sql_statement("DELETE FROM forks WHERE fork_id = -1")

    if dbman.check_table_exists('repo_labels'):
        dbman.execute_sql_statement("DELETE FROM repo_labels WHERE id = -1")

    if dbman.check_table_exists('repo_milestones'):
        dbman.execute_sql_statement("DELETE FROM repo_milestones WHERE id = -1")

    if dbman.check_table_exists('pull_requests'):
        dbman.execute_sql_statement("DELETE FROM pull_requests WHERE id = -1")

    if dbman.check_table_exists('project_commits'):
        dbman.execute_sql_statement("DELETE FROM project_commits WHERE project_id = -1 AND commit_id = -1")

    if dbman.check_table_exists('pull_request_history'):
        dbman.execute_sql_statement("DELETE FROM pull_request_history WHERE id = -1")

    if dbman.check_table_exists('pull_request_comments'):
        dbman.execute_sql_statement("DELETE FROM pull_request_comments WHERE comment_id = -1")

    if dbman.check_table_exists('pull_request_commits'):
        dbman.execute_sql_statement("DELETE FROM pull_request_commits WHERE pull_request_id = -1 AND commit_id = -1")

    if dbman.check_table_exists('issue_labels'):
        dbman.execute_sql_statement("DELETE FROM issue_labels WHERE issue_id = -1 AND label_id = -1")

    if dbman.check_table_exists('issue_events'):
        dbman.execute_sql_statement("DELETE FROM issue_events WHERE event_id -1")

    if dbman.check_table_exists('issue_comments'):
        dbman.execute_sql_statement("DELETE FROM issue_comments WHERE comment_id = -1")

    dbman.close_connection()


if __name__ == "__main__":
    main()